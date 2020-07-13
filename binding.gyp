{
  "targets": [
    {
      "target_name": "binding",
      "sources": [ "binding.cc" ],
      "include_dirs": [ "<!(node -e \"require('nan')\")" ],
      "win_delay_load_hook": "true"
    },
    {
      "target_name": "copy",
      "type": "none",
      "dependencies": [ "binding" ],
      "copies": [
        {
          'destination': '<(module_root_dir)',
          'files': ['<(module_root_dir)/build/Release/binding.node']
        }
      ]
    }
  ]
}
